# Copyright 2018 Cray Inc. All Rights Reserved.

Name: metallb-installer-crayctldeploy
License: Cray Software License Agreement
Summary: metallb deployment ansible role
Group: System/Management
Version: 0.7.0
Release: %(echo ${BUILD_METADATA})
Source: %{name}-%{version}.tar.bz2
Vendor: Cray Inc.
Requires: cray-crayctl
Requires: kubernetes-crayctldeploy

# Project level defines TODO: These should be defined in a central location; DST-892
%define afd /opt/cray/crayctl/ansible_framework
%define roles %{afd}/roles
%define playbooks %{afd}/main
%define modules %{afd}/library
%define runbooks %{afd}/customer_runbooks

%description
This is an Ansible role for the deployment of metalLB.

%prep
%setup -q

%build

%install
install -m 755 -d %{buildroot}%{roles}/
install -m 755 -d %{buildroot}%{runbooks}/
install -m 755 -d %{buildroot}%{playbooks}/

# All roles
cp -r roles/* %{buildroot}%{afd}/roles/

# All customer runbooks
cp -r customer_runbooks/* %{buildroot}%{runbooks}/

# All playbooks
cp -r playbooks/* %{buildroot}%{playbooks}/

%clean
rm -rf %{buildroot}%{roles}/*
rm -rf %{buildroot}%{runbooks}/*
rm -rf %{buildroot}%{playbooks}/*

%files
%defattr(-, root, root)

%{roles}
%{runbooks}
%{playbooks}

%changelog
