import '@styles/ErrorPage.scss'
// import { Router, Route } from '@solidjs/router'


interface ErrorPageProps {
  errorCode: number,
}


export default function NotFound(props: ErrorPageProps) {

  return (
    <div class="error-page" id='NotFound'>
      {props.errorCode} Not Found
    </div>)
}
