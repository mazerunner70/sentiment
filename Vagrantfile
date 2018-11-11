Vagrant.configure("2") do |config|
  # Box name to use
  config.vm.box = "ubuntu/xenial64" # current (2017-12-31) bug - ref: https://askubuntu.com/questions/832137/ubuntu-xenial64-box-password
  config.disksize.size = '40GB'
#  config.ssh.insert_key = true
#  config.ssh.forward_agent = true
#  config.ssh.username = "ubuntu"
#  config.ssh.password = "379a8188cba8c5e64b9a429f"

  # Bento does not work because of a VirtualBox mismatch, new version soon to appear
 # config.vm.box = "bento/ubuntu-16.04"

  # Bring up a separate window for the gui
  config.vm.provider "virtualbox" do |v|
    v.gui = true
    v.cpus = 4
    v.memory = 4096
  end

  # Identify the VM in virtualbox
  config.vm.provider "virtualbox" do |v|
    v.name = "rn-test"
  end

  # From https://www.vagrantup.com/docs/networking/forwarded_ports.html
  config.vm.network "forwarded_port", guest: 80, host: 8080
  
  # Activates Ansible to begin provisioning
  # best practice is here https://www.vagrantup.com/docs/provisioning/ansible_intro.html
  config.vm.define "machine1"

  config.vm.provision "ansible_local" do |ansible|
    ansible.playbook = "ansible/site.yml"
    ansible.groups = {
      "dev_env" => ["machine1"]
    }
    ansible.vault_password_file = "ansible_vault_password.txt"
  end
end
