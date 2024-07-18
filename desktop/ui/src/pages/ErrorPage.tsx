interface ErrorPageProps {
  errorCode: number,
}


export default function NotFound(props: ErrorPageProps) {

  return (
    <div className="error-page" id='NotFound'>
      {props.errorCode} Not Found
    </div>)
}
