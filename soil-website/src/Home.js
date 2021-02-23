import React, { Component } from "react";
import { GoogleLogin } from "react-google-login";

class Home extends Component {

    responseGoogle = (response) => {
        console.log(response);
    }

  render() {
    return (
      <div>
            <h2>Home/Login Page</h2>
            <GoogleLogin buttonText="Login" onSuccess={this.responseGoogle} onFailure={this.response} />
        <p>Example login page, Google login to be added here. Users will only be able to see this page unless they are logged in, then they can access the form page.</p>
      </div>
    );
  }
}

export default Home;