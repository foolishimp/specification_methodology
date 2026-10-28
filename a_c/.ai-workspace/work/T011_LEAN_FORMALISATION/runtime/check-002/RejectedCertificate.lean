import AC.Fixture
set_option debug.skipKernelTC false
example : AC.checkCertificate AC.Fixture.model.dependencies AC.Fixture.model.localKeys AC.Fixture.seeds0 [] = true := by decide +kernel
