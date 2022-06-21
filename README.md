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
* I didn't get around to setting up explicit network or configuration volumes. I hardcoded static IPs on the default Docker network and copied the NginX configuration files in my `Dockerfile`.
* I could iterate this over a couple more days and fill the above gaps.

#### Discussion

I have more experience with Kubernetes for this sort of deployment orchestration. I went with `docker-compose` over Vagrant+Ansible because I wanted to iterate locally on development and testing and VirtualBox doesn't support Apple Silicon. Docker and `docker-compose` works fine on both x86 and ARM. The demo link above is on an x86 EC2 instance in AWS.

For reference I used this Docker [Compose specification](https://docs.docker.com/compose/compose-file/) and [HTTP Load Balancing](https://docs.nginx.com/nginx/admin-guide/load-balancer/http-load-balancer/) for NginX.

I used [Spring Cloud Data Flow](https://dataflow.spring.io/docs/installation/local/docker/) as a real-world docker-compose file ([docker-compose.yml](https://raw.githubusercontent.com/spring-cloud/spring-cloud-dataflow/v2.9.1/src/docker-compose/docker-compose.yml)).
