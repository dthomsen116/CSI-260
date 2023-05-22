"""
Lab: Week 4 Lab – Patients and Procedures

Author: David Thomsen and Sean Sawyers-Abbott
Class: CSI-260
Assignment: Week 4 Lab
Due Date: February 27, 2023

Certification of Authenticity:
I certify that this is entirely my own work, except where I have given
fully-documented references to the work of others. I understand the definition
and consequences of plagiarism and acknowledge that the assessor of this
assignment may, for the purpose of assessing this assignment:
- Reproduce this assignment and provide a copy to another member of academic
- staff; and/or Communicate a copy of this assignment to a plagiarism checking
- service (which may then retain a copy of this assignment on its database for
- the purpose of future plagiarism checking)
"""

from grader import Grader
from lessons import IntroToPython

grader = Grader()
itp_id = grader.register(IntroToPython)

print(itp_id)

#stat_id = grader.register(Statistics)

grader.start_assignment("Tammy", itp_id)
grader.check_assignment("Tammy")
print(grader.assignment_summary("Tammy"))