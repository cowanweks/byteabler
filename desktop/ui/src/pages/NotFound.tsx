import { Button, Result } from 'antd';
import {Link} from "react-router-dom"


export default function NotFound() {

  return (
  <Result
    status="404"
    title="404"
    subTitle="Sorry, the Resource you requested does not exist."
    extra={<Link to="/">
      <Button type="primary">Back Home</Button>
    </Link>}
  />
)}