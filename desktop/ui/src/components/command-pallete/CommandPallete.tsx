import './CommandPallete.scss'


interface CommandPalleteProps {
	title: string,
	children: any
}

export default function CommandPallete(props: CommandPalleteProps){

	return <div id="CommandPallete">
		<header>
			{props.title}
		</header>

		{props.children}

		<footer>
			@ Copyright 2024 ByteTabler
		</footer>
	</div>
}