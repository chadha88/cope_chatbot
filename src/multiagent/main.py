#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from multiagent.crew import Multiagent

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from multiagent.crew import Multiagent

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information
def load_html_template(): 
    with open('src/multiagent/config/newsletter_template.html', 'r') as file:
        html_template = file.read()
        
    return html_template
def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': input('Enter the topic for your newsletter: '),
        'current_year': str(datetime.now().year),
        'personal_message': input('Enter a personal message for your newsletter: '),
        'html_template': load_html_template()
    }
    Multiagent().crew().kickoff(inputs=inputs)
        
    