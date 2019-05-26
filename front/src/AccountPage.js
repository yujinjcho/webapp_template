import React, { Component } from 'react';

import withLogin from './withLogin';

class AccountPage extends Component {

  render() {
    return <div>Account page</div>;
  }
};

export default withLogin(AccountPage);
