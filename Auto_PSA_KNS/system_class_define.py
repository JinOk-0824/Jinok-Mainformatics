from typing import List, Optional


# system component class define
class Component:
    def __init__(
        self,
        no: int = None,
        id: Optional[str] = None,                    # Unique ID [Primary Key]
        name: Optional[str] = None,                  # Component name
        parent: Optional[List['Component']] = None,  # Parent components (FK)
        child: Optional[List['Component']] = None,   # Child components (FK)
        type: str = "",                              # Logic type (e.g., B, +, *)
        component: str = "",                         # Component type (Valve, Pump, etc.)
        status: str = "",                            # Status string
        failtype: str = "",                          # Failure type
        performance: float = 0.0,                    # Performance level
        description: str = "",                       # Description
        lamda: float = 0.0,                          # Failure rate (λ)
        factor: float = 0.0,                         # Multiplying factor
        ccf: bool = False,                           # Common Cause Failure (True/False)
        ccf_re: Optional[List['Component']] = None,  # Child components (FK)
        exception: bool = False                      # Exception flag (True = excluded)
    ):
        self.no = no
        self.id = id
        self.name = name
        self.parent = parent
        self.child = child
        self.type = type
        self.component = component
        self.status = status
        self.failtype = failtype
        self.performance = performance
        self.description = description
        self.lamda = lamda
        self.factor = factor
        self.ccf = ccf
        self.ccf_re = ccf_re
        self.exception = exception

    def __str__(self):
        parent_ids = [p.id if hasattr(p, "id") else str(p) for p in self.parent]
        child_ids = [c.id if hasattr(c, "id") else str(c) for c in self.child]
        return (
            f"Component(\n"
            f"  ID: {self.id}\n"
            f"  NO: {self.no}\n"
            f"  Name: {self.name}\n"
            f"  Parent IDs: {parent_ids}\n"
            f"  Child IDs: {child_ids}\n"
            f"  Type: {self.type}\n"
            f"  Component: {self.component}\n"
            f"  Status: {self.status}\n"
            f"  FailType: {self.failtype}\n"
            f"  Performance: {self.performance}\n"
            f"  Description: {self.description}\n"
            f"  Lamda: {self.lamda}\n"
            f"  Factor: {self.factor}\n"
            f"  CCF: {self.ccf}\n"
            f"  CCF_re: {self.ccf_re}"
            f"  Exception: {self.exception}\n"
            f")"
        )
   