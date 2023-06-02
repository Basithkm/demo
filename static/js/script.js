
{/* <script type="text/javascript"> */}
  function validateForm() {
     
      var name = document.forms["myForm"]["first_name"].value;
      var phone = document.forms["myForm"]["phone_number"].value;
      var email = document.forms["myForm"]["email"].value;
      var password1 = document.forms["myForm"]["password1"].value;
      var password2 = document.forms["myForm"]["password2"].value;

      // Validate phone number
      if (phone.length !== 10) {
          alert("Phone number must be 10 digits long.");
          return false;
      }

      // Validate email
      var emailRegex = /\S+@\S+\.\S+/;
      if (!emailRegex.test(email)) {
          alert("Invalid email address.");
          return false;
      }

      // Check if email already taken
      // You'll need to implement this check on the server side
      if (email === "example@gmail.com") {
          alert("Email address already taken.");
          return false;
      }

      // Validate password
      if (password1 !== password2) {
          alert("Passwords do not match.");
          return false;
      }

      // Validate password strength
      var passwordRegex = /^(?=.*\d)(?=.*[a-zA-Z])[a-zA-Z0-9!@#$%^&*]{8,}$/;
      if (!passwordRegex.test(password1)) {
          alert("Password must be at least 8 characters long and contain at least one digit and one letter.");
          return false;
      }

      return true;
  }
