import React from "react";

import Card from "react-bootstrap/Card";
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";

class GameCard extends React.Component {
  handleSubmit = () => {
    this.props.setTeamOne(this.props.teamOne);
    this.props.setTeamTwo(this.props.teamTwo);
    this.props.history.push("/game");
  };

  render() {
    return (
      <Card
        style={{
          marginLeft: 10,
          marginRight: 10,
          marginTop: 10,
          marginBottom: 10,
          backgroundColor: "#696969"
        }}
        onClick={this.handleSubmit}
      >
        <Container style={{ paddingTop: "5px" }}>
          <Row>
            <Col>
              <Card.Img src={this.props.src} />
            </Col>
            <Col>
              <Card.Img src={this.props.src1} />
            </Col>
          </Row>
        </Container>

        <Card.Body
          style={{
            textAlign: "center",
            color: "white",
            opacity: "0.8"
          }}
        >
          <Card.Title>
            {this.props.teamOne + " vs. " + this.props.teamTwo}
          </Card.Title>
          <Card.Text>{this.props.text}</Card.Text>
        </Card.Body>
      </Card>
    );
  }
}

export default GameCard;
