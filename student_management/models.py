from dataclasses import dataclass, asdict
from datetime import datetime, date
from typing import Dict, Any


class ValidationError(ValueError):
    """Lỗi dữ liệu đầu vào không hợp lệ"""
    pass


def parse_date(date_str: str) -> date:
    try:
        return datetime.strptime(date_str, "%d/%m/%Y").date()
    except:
        raise ValidationError("Date must be in format DD/MM/YYYY")


@dataclass
class Student:
    student_id: str
    full_name: str
    date_of_birth: date
    gender: str
    phone: str
    email: str
    address: str

    def to_dict(self) -> Dict[str, Any]:
        data = asdict(self)
        data["date_of_birth"] = self.date_of_birth.isoformat()
        return data

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "Student":
        return Student(
            student_id=data["student_id"],
            full_name=data["full_name"],
            date_of_birth=parse_date(data["date_of_birth"]),
            gender=data["gender"],
            phone=data["phone"],
            email=data["email"],
            address=data["address"],
        )
