import * as React from 'react';

import './App.less';

import AppLayout from './AppLayout/AppLayout';

class App extends React.Component {
  public render() {
    return (
      <div className="App">
        <AppLayout />
      </div>
    );
  }
}

export default App;
