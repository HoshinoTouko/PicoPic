import * as React from 'react';
import * as ReactDOM from 'react-dom';

import AppLayout from './AppLayout/AppLayout';
import registerServiceWorker from './registerServiceWorker';

import './index.less';

ReactDOM.render(
  <div className="App">
    <AppLayout />
  </div>,
  document.getElementById('root') as HTMLElement
);
registerServiceWorker();

