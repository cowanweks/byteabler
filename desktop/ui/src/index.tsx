/* @refresh reload */
import '@styles/index.scss'
import { render } from 'solid-js/web'
import { Router, Route } from '@solidjs/router'
import { App, Signup, Login, ErrorPage } from '@pages/index'


/** @param
 *
*/
function isAuthorised() {

  return true
}


render(() => {

    return (
          <Router>
                <Route path={["/", "/home"]} component={isAuthorised() ? App : Login} />
                <Route path={["/signin", "/login"]} component={Login} />
                <Route path={["/signup", "/register"]} component={Signup} />
                <Route path="*404" component={() => <ErrorPage errorCode={404} />} />
          </Router>
)}, document.getElementById('root')!);