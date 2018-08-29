import * as React from 'react';
import { match as IMatch, Route, Switch } from 'react-router-dom';

import PostContainer from './container/Post';


const PostRouter = (routerProps: {match: IMatch<{}>}) => {
  const { match } = routerProps;
  return (
    <Switch>
      <Route exact path={`${match.url}`} component={PostContainer} />
    </Switch>
  );
}

export default PostRouter;
