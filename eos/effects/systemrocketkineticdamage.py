# Used by:
# Celestials named like: Wolf Rayet Beacon (6 of 6)
runTime = "early"
type = ("projected", "offline")
def handler(fit, beacon, context):
    fit.modules.filteredChargeMultiply(lambda mod: mod.charge.requiresSkill("Rockets"),
                                       "kineticDamage", beacon.getModifiedItemAttr("smallWeaponDamageMultiplier"),
                                       stackingPenalties = True)
