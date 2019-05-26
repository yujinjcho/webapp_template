import React, { Component } from 'react';
import Container from 'react-bootstrap/Container';

import withLogin from './withLogin';

class AccountPage extends Component {

  render() {
    return (
      <Container>
        <h1>Account</h1>
      </Container>
    );
  }
};

export default withLogin(AccountPage);
