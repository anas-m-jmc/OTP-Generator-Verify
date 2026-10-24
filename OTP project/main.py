from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Store generated OTP
generated_otp = None  #variable


@app.route("/", methods=["GET", "POST"])
def home():
    global generated_otp

    message = ""
    otp_display = ""

    # Generate OTP
    if request.method == "POST" and request.form.get("action") == "generate":
        generated_otp = str(random.randint(100000, 999999))

        # For demonstration only
        otp_display = generated_otp

        message = "OTP generated successfully!"

    # Verify OTP
    elif request.method == "POST" and request.form.get("action") == "verify":
        user_otp = request.form.get("otp")

        if generated_otp is None:
            message = "Please generate an OTP first."

        elif user_otp == generated_otp:
            message = "✅ OTP Verified Successfully!"
            generated_otp = None

        else:
            message = "❌ Invalid OTP. Please try again."

    return render_template(
        "index.html",
        message=message,
        otp_display=otp_display
    )


if __name__ == "__main__":
    app.run(debug=True)