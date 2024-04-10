import '@styles/Login.scss'
import { Button } from '@components/solid-ui/button'


export default function Login() {


    return (<form id='Login' method='post'>
            <div class='btn-controls'>
                <Button variant="secondary" type='button'>Login</Button>
                <Button type='button'>Cancel</Button>
            </div>
        </form>)
}