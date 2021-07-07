# virntup_env_setup

This repository provides a mininet + bmv2 `simple_switch_grpc` wrapper to instantiate a [virntup_4](https://github.com/Mtze/virntup_4) dataplane configurable via [virntup](https://github.com/Mtze/virntup)

> Parts of this wrapper are taken from the [P4 tutorials repository](https://github.com/p4lang/tutorials). 


# Environments 
In the context of virntup and environment (env) describes the link configuration that is present on a target. 
Virntup uses physical link loops to instantiate virtual topologies. An `env.json` file describes which ports on the 
switch are connected to one another and which ports are connected to a host. 

An `env.json` file serves as an input to Virntup! Virntup will create some auxiliary files that then can be used to
configure the target switch as well as the connected hosts. 

The `environments` folder contains some basic configurations that can be used. If you need to create your own 
env, copy the template folder and adapt the files to reflect your target. 


# Target configuration
## BMv2 setup

You can instantiate an environment specified in the `environments` folder with the scripts in the `mininet_env` directory.
As mininet also simulates the hosts, you also  have to copy the `host.json` file, which is created during the `envgen` stage of virntup, to the host. 

After you executed the `mininet_env.py` script with the respective parameters, you will be promoted with the mininet CLI. One BMv2 switch with P4 Runtime will also be started. 
You can connect to the BMv2 switch and deploy virntup_4 to it using the virntup deploy stage. The exact deployment process is documented in the [virntup repository](https://github.com/Mtze/virntup). 
