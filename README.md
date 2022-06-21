## jfapp

#### Super simple load-balanced web app:

* Provisioned using `docker-compose`.
* 2+ Web servers using Flask to respond with instance id.
* **NginX** configured as load balancer (currently unweighted round-robin).

#### Install and run

* [ ] Install Docker. Depending on your Docker version, you may need to install `docker-compose` separately. Otherwise you can use `docker compose ...`.
* [ ] Clone this repo.
* [ ] `docker-compose build`
* [ ] `docker-compose up`
* [ ] Navigate your browser to <http://<HOST>:8080/>. Reload the page a few times, see that the host identification changes.

#### Comments

* An example is running at <http://stretchingzero.com:8080/> (if that times out, try <http://ec2-54-165-123-98.compute-1.amazonaws.com:8080>. An updated DNS record for stretchingzero.com is in progress.