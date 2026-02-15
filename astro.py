import os
import sys
from dotenv import load_dotenv
from rich.console import Console
from rich.panel import Panel
from core.mistral_client import AIClient
from core.executor import Executor
from core.prompts import SYSTEM_PROMPT

# Load environment variables
load_dotenv()

console = Console()

def main():
    # Setup
    api_key = os.getenv("MISTRAL_API_KEY")
    if not api_key or api_key == "your_key_here":
        console.print("[red][!] Error: MISTRAL_API_KEY not found in .env[/red]")
        sys.exit(1)

    consent = os.getenv("CONSENT_REQUIRED", "true").lower() == "true"
    
    astro_ai = AIClient(api_key)
    astro_ai.set_system_prompt(SYSTEM_PROMPT)
    executor = Executor(consent_required=consent)

    console.print(Panel.fit(
        "[bold cyan]ASTRO AI - Autonomous Red Team Assistant[/bold cyan]\n"
        "[dim]Powered by Mistral AI | Dedicated to Kali Linux[/dim]",
        border_style="cyan"
    ))

    while True:
        try:
            user_input = console.input("\n[bold green]ASTRO[/bold green] > ")
            
            if user_input.lower() in ["exit", "quit", "bye"]:
                console.print("[yellow]Shutting down ASTRO AI. Happy Hunting![/yellow]")
                break

            if not user_input.strip():
                continue

            # Step 1: Get AI Recommendation
            with console.status("[cyan]ASTRO is thinking...[/cyan]"):
                command = astro_ai.get_structured_command(user_input)

            console.print(f"[bold yellow][AI Suggestion]:[/bold yellow] `{command}`")

            # Step 2: Execute
            output = executor.execute(command)

            # Step 3: Analyze result
            console.print(f"\n[bold green][Output]:[/bold green]\n{output}")
            
            with console.status("[cyan]Analyzing results...[/cyan]"):
                analysis = astro_ai.chat(f"Analyze this output from command `{command}` and suggest if anything interesting was found:\n{output}")
                console.print(f"\n[bold cyan][Analysis]:[/bold cyan]\n{analysis}")

        except KeyboardInterrupt:
            console.print("\n[yellow]Interrupted. Type 'exit' to quit.[/yellow]")
        except Exception as e:
            console.print(f"[red][!] Error: {str(e)}[/red]")

if __name__ == "__main__":
    main()
