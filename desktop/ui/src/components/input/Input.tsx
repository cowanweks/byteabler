import { JSXElement } from 'solid-js'
import './Input.scss'


// A declaration to define the base input properties.
interface InputProps {
	label: string,
	icon?: JSXElement,
	placeholder: string

}

// A declaration to define the dropdown input properties.
interface DropdownProps extends InputProps {

}

// A declaration to define the password input properties.
interface PasswordProps extends InputProps {

}


/**
 * @file {Input.tsx}
 *
 * 
 * @param
 */
export function Text(props: InputProps) {


	return (<div id='Text' class=''>
				<label for='Text-input'>
					{props.label}
				</label>
				<span id='text-icon'> {props.icon} </span>
				<input id='Text-input' type='text' placeholder={props.placeholder} />
			</div>)
}


/**
 * 
 * @param
 */
export function Dropdown(props: DropdownProps) {


	return (<div id='Text'>
				<label for='Text-input'>
					{props.label}
				</label>
				<input id='Text-input' type='text' placeholder={props.placeholder} />
			</div>)
}


/**
 * 
 * @param
 */
export function PasswordInput(props: PasswordProps) {


	return (<div id='Text'>
				<label for='Text-input'>
					{props.label}
				</label>
				<input id='Text-input' type='password' placeholder={props.placeholder} />
			</div>)
}