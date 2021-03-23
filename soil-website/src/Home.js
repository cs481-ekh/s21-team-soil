import React, { Component } from "react";
import { GoogleLogin } from "react-google-login";
import "./main.css"

class Home extends Component {



    loginSuccess = (response) => {
        console.log(response.getAuthResponse().id_token);
        fetch('http://localhost:8000/authenticate/', {
            method: 'POST',
            headers: {
                'accept': 'application/json',
                'content-type': 'application/json'
            },
            body: JSON.stringify(response.getAuthResponse().id_token)
        })
    }

    loginFailure = (response) => {
        console.error(response);
    }

  render() {
    return (
      <div className="home-page">
         <div className="center">
              <div className="center">
                <h2>Home/Login Page</h2>
              </div>
              <div className="center-google">
                <GoogleLogin buttonText="Login" clientId="91335092244-a8nui54bma999p0f0f61uklj8095v6cl.apps.googleusercontent.com" onSuccess={this.loginSuccess} onFailure={this.loginFailure} />
              </div>
            <p>Example login page. Users will only be able to see this page unless they are logged in, then they can access the form page.</p>
          </div>
      </div>
    );
  }
}

export default Home;