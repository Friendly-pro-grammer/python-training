from django.core.management.base import BaseCommand
from user.models import Role


ROLES = [
    {
        "roleName": "Super Admin",
        "accessModules": [
            "users",
            "roles",
            "permissions",
            "organizations",
            "audit-logs",
            "analytics",
            "billing",
            "settings",
            "dashboard",
        ],
    },
    {
        "roleName": "Admin",
        "accessModules": [
            "users",
            "roles",
            "permissions",
            "organizations",
            "audit-logs",
            "analytics",
            "dashboard",
        ],
    },
    {
        "roleName": "Tech Lead",
        "accessModules": [
            "projects",
            "repositories",
            "deployments",
            "environments",
            "monitoring",
            "logs",
            "analytics",
            "dashboard",
        ],
    },
    {
        "roleName": "Developer",
        "accessModules": [
            "projects",
            "repositories",
            "deployments",
            "environments",
            "logs",
            "dashboard",
        ],
    },
    {
        "roleName": "DevOps Engineer",
        "accessModules": [
            "repositories",
            "deployments",
            "environments",
            "infrastructure",
            "monitoring",
            "logs",
            "dashboard",
        ],
    },
    {
        "roleName": "QA Engineer",
        "accessModules": [
            "projects",
            "test-runs",
            "bug-tracking",
            "reports",
            "logs",
            "dashboard",
        ],
    },
    {
        "roleName": "Security Engineer",
        "accessModules": [
            "users",
            "permissions",
            "audit-logs",
            "security",
            "monitoring",
            "reports",
            "dashboard",
        ],
    },
    {
        "roleName": "Data Engineer",
        "accessModules": [
            "data-pipelines",
            "datasets",
            "analytics",
            "monitoring",
            "logs",
            "dashboard",
        ],
    },
    {
        "roleName": "Product Manager",
        "accessModules": [
            "projects",
            "analytics",
            "reports",
            "users",
            "dashboard",
        ],
    },
    {
        "roleName": "Intern",
        "accessModules": [
            "projects",
            "repositories",
            "test-runs",
            "bug-tracking",
            "dashboard",
        ],
    },
    {
        "roleName": "Viewer",
        "accessModules": [
            "reports",
            "analytics",
            "dashboard",
        ],
    },
]


class Command(BaseCommand):
    help = "Seed default roles"

    def handle(self, *args, **kwargs):
        for role_data in ROLES:
            Role.objects.get_or_create(
                roleName=role_data["roleName"],
                defaults={
                    "accessModules": role_data["accessModules"],
                    "active": True,
                },
            )

        self.stdout.write(
            self.style.SUCCESS("Roles created successfully!")
        )