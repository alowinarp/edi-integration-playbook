import os
import sys

SRC_FOLDER = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..",
    "src",
)

sys.path.insert(0, SRC_FOLDER)


from edi_997 import generate_997
from edi_parser import parse_edi
from fastapi.testclient import TestClient
from main import app
from validation.validate_850 import validate_850


client = TestClient(app)

INPUT_FOLDER = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..",
    "input",
)

def read_sample_850(file_name: str) -> str:
    path = os.path.join(INPUT_FOLDER, file_name)

    with open(path, "r") as open_file:
        return open_file.read()


def test_generate_997_accepts_a_valid_850() -> None:
    parsed = parse_edi(read_sample_850("valid_850.txt"))
    errors = validate_850(parsed.segments)

    acknowledgment = generate_997(
        parsed.segments,
        errors,
        parsed.delimiters,
    )
    assert "ST*997*" in acknowledgment
    assert "AK1*PO*101" in acknowledgment
    assert "AK2*850*0001" in acknowledgment
    assert "AK5*A" in acknowledgment
    assert "AK9*A*1*1*1" in acknowledgment


def test_generate_997_rejects_an_invalid_850() -> None:
    parsed = parse_edi(read_sample_850("invalid_850.txt"))
    errors = validate_850(parsed.segments)
    
    acknowledgment = generate_997(
        parsed.segments,
        errors,
        parsed.delimiters,
    )

    assert "AK5*R*5" in acknowledgment
    assert "AK9*R*1*1*0" in acknowledgment


def test_post_850_endpoint_accepts_a_valid_850() -> None:
    edi_text = read_sample_850("valid_850.txt")

    response = client.post(
        "/edi/850",
        content=edi_text,
        headers={"Content-Type": "text/plain"},
    )

    assert response.status_code == 200
    
    body = response.json()

    assert body["validation_status"] == "accepted"
    assert (
        body["purchase_order"]["purchase_order_number"]
        == "PO10001"
    )
    assert "AK5*A" in body["acknowledgment_997"]