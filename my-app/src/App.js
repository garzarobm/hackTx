import React, {useState} from 'react';
//import logo from './logo.svg';
import './App.css';
import 'bootstrap/dist/css/bootstrap.css';
import {Container, Row, Col} from 'reactstrap';
import {Dropdown, DropdownItem, DropdownMenu, DropdownToggle} from 'reactstrap';
import { ListGroup, ListGroupItem } from 'reactstrap';


function App() {
  const [dropdownOpen, setDropdownOpen] = useState(false);

  const toggle = () => setDropdownOpen(prevState => !prevState);
  const toggle2 = () => setDropdownOpen(prevState => !prevState);

  return (
    <div className="App">
      {/* <header className="App-header"> */}
        {/* <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a> */}
        <Container>
          <br />
          <br />
          
          <Row>
            
            <Col>
              <Dropdown isOpen={dropdownOpen} toggle={toggle}>
                <DropdownToggle caret>
                  Source
                  </DropdownToggle>
                <DropdownMenu>
                  {/* <DropdownItem header>Header</DropdownItem>
                  <DropdownItem>Some Action</DropdownItem>
                  <DropdownItem disabled>Action (disabled)</DropdownItem>
                  <DropdownItem divider /> */}
                  <DropdownItem>DFW</DropdownItem>
                  <DropdownItem>Hobby</DropdownItem>
                  {/* <DropdownItem>Quo Action</DropdownItem> */}
                </DropdownMenu>
              </Dropdown>
            </Col>

            <Col>
              <Dropdown isOpen={dropdownOpen} toggle={toggle2}>
                <DropdownToggle caret2>
                  Destination
                  </DropdownToggle>
                <DropdownMenu>
                  {/* <DropdownItem header>Header</DropdownItem>
                  <DropdownItem>Some Action</DropdownItem>
                  <DropdownItem disabled>Action (disabled)</DropdownItem>
                  <DropdownItem divider /> */}
                  <DropdownItem>DFW</DropdownItem>
                  <DropdownItem>Hobby</DropdownItem>
                  {/* <DropdownItem>Quo Action</DropdownItem> */}
                </DropdownMenu>
              </Dropdown>
            </Col>
           
          </Row>
          <br />
          <br />

          <Row>
            <ListGroup>
              <ListGroupItem>Cras justo odio</ListGroupItem>
              <ListGroupItem>Dapibus ac facilisis in</ListGroupItem>
              <ListGroupItem>Morbi leo risus</ListGroupItem>
              <ListGroupItem>Porta ac consectetur ac</ListGroupItem>
              <ListGroupItem>Vestibulum at eros</ListGroupItem>
            </ListGroup>
          </Row>
        </Container>
      
        {/* </header> */}

    </div>
    
  );
}



export default App;
