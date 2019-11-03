import React from "react";

import Navbar from "react-bootstrap/Navbar";
import Nav from "react-bootstrap/Nav";
import Form from "react-bootstrap/Form";
import Button from "react-bootstrap/Button";

class GlobalNavbar extends React.Component {
  render() {
    return (
      <div className="Homepage">
        <>
          <Navbar bg="dark" variant="dark">
            <Nav className="mr-auto">
              <Nav href="/">Home</Nav>
              <Nav href="/betnow">Bet Now</Nav>
              <Nav href="/about">About</Nav>
            </Nav>
            <Form inline>
              {this.props.username === undefined ||
              this.props.username === null ? (
                <Button to="/login" variant="outline-info">
                  Log-in
                </Button>
              ) : (
                <Button variant="outline-info" onClick={this.reloadHome}>
                  Hello, {this.props.username}
                </Button>
              )}
            </Form>
          </Navbar>
        </>
      </div>
    );
  }
}

export default GlobalNavbar;
