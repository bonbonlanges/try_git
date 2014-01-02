# prior to usage, Fabric must be installed first
# $ pip install fabric

# deployment
# $ fab prepare_deployment:<your_branch_name>
# $ fab deploy

from fabric.api import local

def prepare_deployment(branch_name):
	"""
	This will run the tests, commit branch change, 
	and merge them into master. At this point, a simple "git pull" 
	in the production area becomes the deployment.

	'website' is the name of our app
	"""
    local('python manage.py test website')
    local('git add -p && git commit')
    local('git checkout master && git merge ' + branch_name)

from fabric.api import lcd

def deploy():
	"""
	This will pull the changes from the development master branch, 
	run any migrations made, run tests, and restart webserver. All 
	in one simple command from the command line. If one of those 
	steps fails, the script stops and reports what happened. 

	Once the issue has been fixed, there is no need to run the steps manually.
	Simply rerun the deploy command and all will be well.
	"""
	with lcd('/path/to/my/prod/area/'): #TODO
        local('git pull /my/path/to/dev/area/') #TODO
        local('python manage.py migrate website')
        local('python manage.py test website')
        local('/my/command/to/restart/webserver') #TODO