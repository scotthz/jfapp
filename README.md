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
* The number of web servers is not yet automatically scalable. To add more web servers:
  * [ ] Add additional `appN` entries in `services` in `docker-compose.yml`.
  * [ ] Add additional `server` entries in `upstream jflb` in `nginx/jfapp.conf`.
* I developed on ARM  and tested on x86. The webserver is not currenly multi-architecture. The `appx` image in `scotthz.jfrog.io` currently supports x86 only.
* You'll need credentials to access `scotthz.jfrog.io`. 
* This was thrown together in about 2 days. Please don't judge harshly.