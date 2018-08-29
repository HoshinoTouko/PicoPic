import * as React from 'react';
import * as ReactDOM from 'react-dom';
import Helmet from 'react-helmet';

import AppLayout from './AppLayout/AppLayout';
import registerServiceWorker from './registerServiceWorker';

import './index.less';

ReactDOM.render(
  <div className="App">
    <Helmet title='PicoPic' />
    <AppLayout />
  </div>,
  document.getElementById('root') as HTMLElement
);
registerServiceWorker();

