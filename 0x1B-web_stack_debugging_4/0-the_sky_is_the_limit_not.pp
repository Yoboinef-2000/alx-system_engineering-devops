# This puppet script is supposedly going to fix
# the errors associated with the huge amount
# of failed requests.

# But the problem is my nginx server is not showing
# any failed-request isssues so I am just going off
# what the potential issue of the server in the exercise 
# is supposd to be

# When I went to nginx in /etc, everything was commmented out.
# One of the comments was that ulimit was set to 4096.
# So I am just going to play around with that and whatever sticks, sticks.

exec {'letsSeeIfThisWorks':
  command  => 'sudo sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/" /etc/default/nginx',
  before   => Exec['reloooadTheThing'],
  provider => shell,
}

exec { 'reloooadTheThing':
  command  => 'sudo service nginx reload',
  provider => shell,
}
