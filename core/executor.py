import subprocess
import os

class Executor:
    """
    Executes shell commands on the host system.
    Designed for Kali Linux / Red Team operations.
    """
    def __init__(self, consent_required=True):
        self.consent_required = consent_required

    def execute(self, command):
        """
        Executes a command and returns the output.
        """
        if self.consent_required:
            print(f"\n[!] ASTRO AI wants to run: {command}")
            confirm = input("Confirm execution? (y/n): ").lower()
            if confirm != 'y':
                return "Execution cancelled by user."

        try:
            # Running in shell=True for complex piping commands common in Kali
            process = subprocess.Popen(
                command,
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            stdout, stderr = process.communicate()
            
            output = stdout if stdout else ""
            if stderr:
                output += f"\n[ERROR]: {stderr}"
            
            return output if output else "[Success: No output]"
        except Exception as e:
            return f"[CRITICAL ERROR]: {str(e)}"
