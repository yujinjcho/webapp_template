import React, { Component } from 'react';

import withLogin from './withLogin';

class MainPage extends Component {

  render() {
    const { accountId } = this.props;
    const msg = `Logged in with ${accountId}`
    return <div> {msg} </div>
  }
};

export default withLogin(MainPage);
