import React, { Component } from 'react';
import Container from 'react-bootstrap/Container';

import withLogin from './withLogin';

class MainPage extends Component {

  render() {
    const { accountId } = this.props;
    const msg = `Logged in with account id: ${accountId}`
    return (
      <Container>
        <h1>Dashboard</h1>
        <div> {msg} </div>
      </Container>
    );
  }
};

export default withLogin(MainPage);
