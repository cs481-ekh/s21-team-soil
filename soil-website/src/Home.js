import React, { Component } from "react";
import { GoogleLogin } from "react-google-login";

class Home extends Component {



    loginSuccess = (response) => {
        console.log(response.getAuthResponse().id_token);
    }

    loginFailure = (response) => {
        console.error(response);
    }

  render() {
    return (
      <div>
            <h2>Home/Login Page</h2>
            <GoogleLogin buttonText="Login" clientId="91335092244-a8nui54bma999p0f0f61uklj8095v6cl.apps.googleusercontent.com" onSuccess={this.loginSuccess} onFailure={this.loginFailure} />
        <p>Example login page, Google login to be added here. Users will only be able to see this page unless they are logged in, then they can access the form page.</p>
      </div>
    );
  }
}

export default Home;