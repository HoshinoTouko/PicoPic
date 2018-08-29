import * as React from 'react';
import { BrowserRouter, HashRouter, Redirect, Route, Switch } from 'react-router-dom';

import HomeContainer from '../apps/home/container/Home';
import PostRouter from '../apps/post/router';

const DEV = process.env.NODE_ENV !== 'production';
const DEBUG = process.env.DEBUG === 'true';

const WorkingRouter = (DEV && !DEBUG) ? HashRouter : BrowserRouter;

class AppRouter extends React.Component<{}, {}>{
  public render() {
    return (
      <WorkingRouter>
        <Switch>
          <Route exact path='/' component={HomeContainer} />
          <Route path='/post' component={PostRouter} />
          <Redirect to='/' />
        </Switch>
      </WorkingRouter>
    )
  }
}

export default AppRouter;
