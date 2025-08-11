# Rules for Janus project - New contributor's handbook






























Before starting anything, you must read and approve these few rules by commenting: "I, [name], read, analyzed, familiarized myself, questioned, asked questions to better understand, understand and approve these principles, methodologies, rules and procedures and will abide by them."

# [Principles, Guidelines & Methodologies](https://gitlab.com/jdosec/janus/-/blob/main/documentation/tools/README.md)
See more rules, suggestion, guidelines, use cases, etc. in https://gitlab.com/jdosec/janus/-/tree/main/archive /trine.wiki
## Priorities
### Do less but in the BEST way
- Test >>> Quantity (Functionality): Tests (functionality and security) increase the reliability and re-usability of the project
- Portability >>> Quantity (Functionality)
- Usability >>> Quantity (Functionality)
- Maintainability >>> Quantity (Functionality)
- Modularity >>> Quantity (Functionality): we only use a single repository for ease of use. Do split, organize each self-sustainable tool/feature as a separate project in a modular, publishable and reusable fashion
- Quality >>> Quantity (Functionality)
- Security >>> Quantity (Functionality): If it is unsafe to run the project, it has no value within our community
- Re-usability and repeatability for others >>> Quantity (Functionality). If it ain't reusable, modular ... it is not usable ... it ain't done. Value=0

### If it ain't automated ... it ain't done. Value=0
- Automated >>> Manual: Human time is the rarest resource. Don't waste it, assume it's scarce.

### Autonomy as a team member
- Autonomous & pro-active: Ask, improve, augment the handbook, collaborate, etc. don't "just wait" for things to happen. If you don't believe in the project, it is fine ... don't join it, do something else.
- Uniformity of tools: follows kiss, repeatability, etc. (single kms, single dev platform, single ...). This affect maintainability, the cost of joining the project, etc. It should be trivial to join the project after you leave and at most, one should only read the handbook.
- Integrate & Improve >>> Reinvent the wheel: Check, learn from and integrate with previous productions (see [archives](https://gitlab.com/jdosec/janus/-/tree/main/archive?ref_type=heads) there are templates for meetings, for reference id sheets, playbooks, use cases, etc.).
- Integrate >>> Reinvent the wheel: the less you code, the less we have to maintain yourself. But do it securely. Appropriate yourself the external codes, scripts, references. Make it yours, you should be able to justify, explain every single line, every single word.

### If it ain't reusable ... it ain't done
- No added valued delivered tangible deliverable = NO VALUE = 0/20 (if the cost is lower for others to ignore your "contribution" and start from scratch than to use it as "delivered" ... it means it has no value; whatever the reason be it to ensure maintainability, adapt, customize, ensure security ...). Ask yourself: can I just publish it as is and 1. be proud of it 2. lots of people will use it as is 3. lots of people will want to contribute/build upon it instead of starting from scratch. Then you reached the minimum bar. Millions of 1 minute effort 1-liner snippets to do the smallest of functionality have reached that bar. If deliverable is not stand alone, complete (even if small), secure, re-usable it is a huge failure and should be canceled/advertised/accepted as such.

# Rules

## Communications
Awaiting our own services, monitored, run, etc. by ourselves ("eat what you cook" principle):
- default written discussion: https://framateam.org/torchlights-dmz/channels/diasciosrl-rd
- default visio: https://framatalk.org/DiaScioRD

## Repositories, accounts, etc.
- Ask @jdosec  to create the account, repositories etc. (gitlab, dockerhub, vagranthub, overleaf, mail, ...) necessary. Re-usability is of the essence, we need to have access and control to the deliverables before, during and after your participation to the project. Anything that would rely on your private accounts cannot sustain for the project and shouldn't be used.
- exchange of credentials: should be using our credentials management service (still waiting for deployment). Master creds exchanged encrypted with public key cryptography. Share your public key in the repository in a structured fashion, validate in person your fingerprints.

## Filenames
- Ensure portability (multi-platform): Ensure anything (including this wiki's page) are multi-platform (linux, windows, mac, android, ...) filesystem compatible (e.g. do not include characters in names that won't be supported on one of these platform)

## Budget/Time management
- Any participant has to measure time consumption of pomodoro bursts (meaning 100% full focused on project, anything else does not count)
- Time is measured at minimum with weekly pomodoro charts https://drive.google.com/file/d/1uHIVmFTPXHWKozVGZ9-fxugkxChQjhq7/view?usp=drive_link (you can also have a fine grained measurement per task, issue, workpackages etc. Gantt etc. in addition to this pomodoro chart)

## LLM/AI/... and thesis, ...
- Never ask others to work/invest their time and effort on what you didn't: If it's AI generated, do not ask someone to review it. Your supervisor's review's objective is to help you improve your skills (by helping you fixing your document). Your document is not the end purpose. Correcting or improving an AI is not the purpose.
- LLMs etc. are useful. You need to stay in charge and be the creator.
Example of usages to consider: getting extra reviews
target_audience={student, professor, practitioner, researcher} at master level or above in cybersecurity
for each role in target_audience:
do
Assume you are a $role. <insert more about role activities, needs, ...: e.g.:"You are teaching cybersecurity.">
Below, after the "---------" you'll find part of a master thesis in cybersecurity.
<insert: part of the document you are submitting to get feedback. e.g. "It is the document overview of the introduction ">
<insert: what is the theme of the document.: e.g. "The document is about defense mechanisms against phishing.">
What would you recommend?
Write your recommendations as bullet points containing 1. the paragraph or sentence for which you have a remark. 2. the claim or title of your remark. 3. 2-3 short sentence to elaborate with support and warrant to that claim. 4. a recommendation to fix the issue.
Take the maximum amount of time to think deeply about it. Your remarks should be mostly about the best way to present an argumentation in a scientific document, a discourse in a written report or thesis. But also on cybersecurity aspects, missing notions etc.
Make sure the recommendations of the following sources are applied:
- "Éléments de rédaction scientifique en informatique" by Hadrien Mélot from Faculté des Sciences, UMONS
- "The 88 keys for identifying problems in logic and expression of thought in texts" Victor Thibaudeau, Faculty of philosophy, Laval University, 1998
Please limit to 1 remark per paragraph of the provided text
---------

## KMS
- Logseq is the kms of choice


## Gitlab project management
- Gitlab issues, milestones, etc. is the platform used for project management
- Any workpackage, task, activity, etc. is recorded in it (issue for example)

## Git
- **Activate githook  [commands here](https://gitlab.com/jdosec/janus/-/blob/main/.githooks/README.md?ref_type=heads)**
- **Don't push on the main branch**
- **Don't merge your own branch**
- **Don't merge without a full review with 2 other peoples**
- **Creates a branch in reference to what you do with a good name**
- **Pull and test your work just before creating a merge request**

## Meetings
- Any meeting shall follow [Meeting's bloody meeting](https://en.wikipedia.org/wiki/Meetings,_Bloody_Meetings)'s guidelines including having a plan before the meeting, announcing it and filling it with minutes shared after the meeting
- Any non-repetitive appointment will follow a 3-way handshake to be confirmed which terminates with an ics calendar invitation.
- Any meeting is associated to minutes and an ics calendar event that provides all the links to all the resources expected to be necessary for said meeting. Said ICS should contain all elements (or links to) relevant for the meeting (including meeting plan, expected input, output etc. see meetings below). The title, like any mail, file, document, etc. should be chosen to be useful to identify, manage, etc. the meeting. "Meeting created via outlook" or "3-way handshake meeting" is useless as a title. It would be like a book title being "Printed on paper" instead of "Lord of the Rings".
- Minimum 1 meeting per week with other research lab participants: Synchronize your watches. Ensure you DO work collaboratively, you DO help each other, you DO integrate and work on the same project
- Max target duration of a meet should be 1h: if more is required, probably the plan wasn't done properly and several meetings should be necessary on different sub parts


## Delivering workpackages/projects
- Takes time -> needs to be planned, scheduled, resources allocated, ...
- Has many components (documentation, code, applied community conference white paper, applied community conference white paper's slides, recorded demos, hands one workshops, handover sessions, ...) which have to be "usability tested" i.e. handover. You should actively demonstrate that someone with no knowledge of the project, joining on that day, would be able to easily appropriate, run, continue and built upon it. Because that is the objective to reach. Anything less than that is useless.
- Is essential (no delivery = ... no value delivered = no value)
- During final delivery: everyone in the research group should have understood (any tangible deliverable: thesis, documentation, videos, etc.) and be able to safely replicate your results (workshop): "Yes but it works on my machine" = "It works on my stomach, I ate your pizza, I didn't deliver it" = no delivery = 0/20 as a grade

## Coding style
- Default & Python: https://peps.python.org/pep-0008/

## References
- Any reviewed reference needs to have it's corresponding [review/id sheet](https://docs.google.com/presentation/d/1netzbVuA_6SSueuISigPa-KbD2fRnym7i_s4VrlpDJA/edit#slide=id.g106aecda60e_0_40) stored in the kms in a single format

# Procedures

# Learning / Must Reads
Please share here the best resources you have on a topic. The ones with the most efficacy and efficiency. Shorter & easier = better. Many keywords don't have a best resource yet, they need one.

## Meetings
- Meetings bloody meetings https://en.wikipedia.org/wiki/Meetings,_Bloody_Meetings https://www.youtube.com/watch?v=dsChGa-Dako https://www.youtube.com/playlist?list=PLn8FlhZQ69X97ViO1qVyd40IHykgZjgvI
- 5 stage plan for shorter and more productive meetings from John Cleese's 1976 training video "Meetings, bloody meetings"
	- {{video(https://youtu.be/dsChGa-Dako?feature=shared&t=1620)}}
	- Plan
		- Clear your mind about the precise objectives of the meeting
			- Be clear why you need it
			- And list the subjects
	- Inform
		- (output) Make sure everyone knows
			- What is being discussed
			- Why
			- And what you want from the discussion
		- (input) Both
			- Anticipate
				- what
					- information
					- and people
				- may be needed
			- and make sure there are there
	- Prepare
		- Logical sequence
			- The logical sequence of items
		- Time
			- The time allocation to each item
				- on the basis of its importance
				- not its urgency
	- Structure and control
		- 3 stages in this chronological order
			- Evidence
			- Interpretation
			- Action
		- Stop people
			- jumping ahead
			- or going back over old ground
	- Summarize and record (decisions)
		- Summarize all decisions
			- And record them straight away
				- With the name of the person responsible for the action

## Project methodology
- Project management glossary lexicon : https://www.pmi.org/standards/lexicon
- Scrum guide
  * https://scrumguides.org/
- GQM
  * https://www.cs.umd.edu/users/mvz/handouts/gqm.pdf
- K.I.S.S.: Keep It Simple and Stupid
  * https://devopscon.io/continuous-delivery-automation/kiss-in-action-simplify-your-continuous-delivery-pipeline-architecture/
- P.D.C.A.: Plan, Do, Check, Act
    * https://www.productplan.com/glossary/pdca-cycle/#:~:text=The%20PDCA%20cycle%20is%20a,are%20arranged%20in%20a%20circle.
- K.P.I.
    * https://www.grow.com/blog/how-to-use-smart-goals-to-build-your-kpis
    * https://handbook.gitlab.com/handbook/company/kpis/
- R.A.C.I.
- S.M.A.R.T.
- [\*Wikipedia contributors. (2023, November 1). Expectancy theory. In Wikipedia, The Free Encyclopedia. Retrieved 20:14, December 13, 2023, from \*https://en.wikipedia.org/w/index.php?title=Expectancy_theory&oldid=1182997575](https://en.wikipedia.org/w/index.php?title=Expectancy_theory&oldid=1182997575)
    * V.I.E. (Vroom)
- Scientific Method https://en.wikipedia.org/wiki/Scientific_method

### Automation && DevOps concepts
- Security as Code
  * https://about.gitlab.com/blog/2020/03/12/how-to-security-as-code/
- C.a.C. : Configuration as Code
- I.a.C. : Infrastructure as Code
- E.a.C. : Everything as Code
      * https://octopus.com/blog/what-is-everything-as-code
- C.A.L.M.S.
      * https://www.atlassian.com/devops/frameworks/calms-framework
- T.D.D. / T.D.I. : Test Driven Infrastructure
- C.I./.C.D.: Continuous Integration / Continuous Deployment
- DevSecOps
      * DevSecOps Fundamentals Guidebook: DevSecOps Tools & Activities (https://dodcio.defense.gov/Portals/0/Documents/Library/DevSecOps%20Fundamentals%20Guidebook-DevSecOps%20Tools%20and%20Activities_DoD-CIO_20211019.pdf)
      * https://about.gitlab.com/topics/devsecops/
      * https://www.redhat.com/fr/topics/devops/what-is-devsecops

### Security testing
- S.A.S.T.
- D.A.S.T.
- R.A.S.P.
- I.A.S.T.
      * https://www.softwaresecured.com/post/what-do-sast-dast-iast-and-rasp-mean-to-developers
      * pre-commit
        * Threat modeling
        * IDE security plugins
        * pro-commit hooks
        * Peer code review
      * commit
        * Static code analysis
        * Security unit tests
        * Dependency management
        * Container security
      * acceptance
        * Dynamic security tests
        * Acceptance tests
        * Infrastructure as code
        * Configuration management
      * production
        * Server hardening
        * Runtime protection
        * Secrets management
        * Safety checks
      * operations
        * Blameless postmortem
        * Continuous monitoring
        * Fire drills
        * Threat intelligence
### Project assumption/objectives
  * Minimal human cost
    * KISS
      * Minimal technology stack
  * Maximum reusability
    * Delivery focused
    * Everything as code
    * Modular
    * Open source
  * Security by design
  * Privacy by design
  * Open by design
 
## CaC & Ansible
  * [Ansible for DevOps, Jeff Geerling](https://leanpub.com/ansible-for-devops)
    * Get it for free: https://leanpub.com/ansible-for-devops/c/CTVMPCbEeXd3
    * Get the corresponding videos for free (Ansible 101): https://www.youtube.com/playlist?list=PL2_OBreMn7FplshFCWYlaN2uS8et9RjNG
    * https://www.ansiblefordevops.com/
    * https://github.com/geerlingguy/ansible-for-devops-manuscript
    * https://github.com/geerlingguy/ansible-for-devops

## Virtualization
### Proxmox
- https://www.proxmox.com/en/proxmox-virtual-environment/overview
### Virtualbox

## Orchestration
### Docker
- [Docker Essentials](https://www.udemy.com/course/docker-essentials)
### Vagrant
### Terraform
### Gitlab CI/CD
### Travis

## Image building
### Packer
### Pre-seeding

## Programming
### Python
### Bash

## Unit testing
### Molecule
### BATS
- https://github.com/bats-core/bats-core
### PyUnit

## Versioning
### Git
* https://learngitbranching.js.org/

## Hosting
### Hetzner
- https://docs.hetzner.com/robot/dedicated-server/troubleshooting/hetzner-rescue-system/
- https://docs.hetzner.com/storage/storage-box/general
- https://docs.hetzner.com/robot/dedicated-server/operating-systems/installimage
- https://dazeb.dev/how-to-add-a-hetzner-storagebox-to-proxmox-with-smb-cifs/
- https://github.com/kpma1985/ansible_proxmox_hetzner https://forum.proxmox.com/threads/ansible-playbook-for-hetzner-incl-opnsense.116732/
-------------------------------------------------------------------


- [x] I, Delvigne Antoine, read, analyzed, questioned, understand and approve these principles, methodologies, rules and procedures and will abide by them.
- [x] I, Bruyere Mathis, read, analyzed, questioned, understand and approve these principles, methodologies, rules and procedures and will abide by them.
- [x] I, Smet Maeve, read, analyzed, questioned, understand and approve these principles, methodologies, rules and procedures and will abide by them.
- [x] I, Querinjean Arnaud, read, analyzed, questioned, understand and approve these principles, methodologies, rules and procedures and will abide by them.
- [x] I, De Sousa Barros Leal Mendo, read, analyzed, questioned, understand and approve these principles, methodologies, rules and procedures and will abide by them.
- [x] I, Bakhat Ilyas, read, analyzed, questioned, understand and approve these principles, methodologies, rules and procedures and will abide by them.
