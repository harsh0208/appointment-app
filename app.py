def cancel_appointment(status):
    if status == "booked":
        return "Cancelled"
    return "Cannot cancel"


if __name__ == "__main__":
    print(cancel_appointment("booked"))