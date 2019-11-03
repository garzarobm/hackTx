import React from 'react';
import logo from './logo.svg';
import './App.css';
import DatePicker from "react-datepicker";

import "react-datepicker/dist/react-datepicker.css";

class FlavorForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = {valueOrigin: 'DFW', valueDest:'DFW', date: new Date()};

    this.handleChangeDest = this.handleChangeDest.bind(this);

    this.handleChangeOrigin = this.handleChangeOrigin.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChangeOrigin(event) {
    this.setState({valueOrigin: event.target.value});
  }

  handleChangeDest(event) {
    this.setState({valueDest: event.target.value});
  }

  handleChangeDate = date => {
    this.setState({
      date: date
    });
  };

  handleSubmit(event) {
    alert('Your origin is: ' + this.state.valueOrigin + '\nYour destination is: ' + this.state.valueDest + '\n Your date is: ' + new Intl.DateTimeFormat('en-US').format(this.state.date));
    event.preventDefault();
  }




  render() {
    return (
      <form onSubmit={this.handleSubmit}>
        <label>
          Pick your origin:
          <select value={this.state.valueOrigin} onChange={this.handleChangeOrigin}>
            <option value="DFW">Dallas-Fort Worth, TX</option>
            <option value="ORD">Chicago, IL</option>
            <option value="JFK">New York City, NY</option>
            <option value="LAX">Los Angeles, CA</option>
          </select>
        </label>

        <label>
          Pick your destination:
          <select value={this.state.valueDest} onChange={this.handleChangeDest}>
            <option value="DFW">Dallas-Fort Worth, TX</option>
            <option value="ORD">Chicago, IL</option>
            <option value="JFK">New York City, NY</option>
            <option value="LAX">Los Angeles, CA</option>
          </select>
        </label>
        <DatePicker selected={this.state.date} onChange={this.handleChangeDate}/>
        <input type="submit" value="Submit" />
      </form>
    );
  }
}

export default FlavorForm;
