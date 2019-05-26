import React, { Component } from 'react';
import { BrowserRouter as Router, Route } from 'react-router-dom';

import MainPage from './MainPage';
import Login from './Login';
import Logout from './Logout';
import Auth from './Auth';
import AccountPage from './AccountPage';

class App extends Component {
  render() {
    return (
      <div>
        <Router>
          <>
            <Route exact path="/" component={MainPage} />
            <Route exact path="/account" component={AccountPage} />
            <Route exact path ="/login" component={Login} />
            <Route exact path ="/logout" component={Logout} />
            <Route exact path ="/auth" component={Auth} />
          </>
        </Router>
      </div>
    );
  }
}

export default App;
