# MetalLB 

This was used only thru shasta-1.3.  It was deprecated with shasta-1.4 (pre csm-1.0).

This sets up MetalLB in the cluster to support LoadBalancer services. 

https://metallb.universe.tf/

## Roles:
metallb - Installs the MetalLB config-map, controller deployment, and speaker daemon set.
          The config map includes the peer information as well as configuration of the address pools for NMN, HMN, HSN, and the two customer_access pools if they are defined in customer_var.yml.

metallb-bgp-reset - Runs the command 'clear ip bgp *' on the switches to reset the peering sessions on a fresh installation.

## Customer Runbooks

metallb-localize.yml - Calls the metallb role.  This is included in the main_localize.yml runbook.  It uses values from networks.yml and customer_var.yml

This runbook can be run independently:

ansible-playbooks /opt/cray/crayctl/ansible_framework/customer_runbooks/metallb-localize.yml

## Playbooks

A set of playbooks are available to check status on the leaf and spine switches.  This is easier for automation such as CT test because the credentials are handled by ansible.

leaf-bgp-routes.yml -  Shows the current BGP routes on the leaf switch
leaf-bgp-status.yml -  Shows the current BGP peer status on the leaf switch
spine-bgp-routes.yml - Shows the current BGP routes on the spine switches
spine-bgp-status.yml - Shows the current BGP peer status on the spine switches

Each of these playbook can be run independently:

ansible-playbooks /opt/cray/crayctl/ansible_framework/main/leaf-bgp-status.yml

