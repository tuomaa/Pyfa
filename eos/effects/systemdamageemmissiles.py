# Used by:
# Celestials named like: Magnetar Effect Class (6 of 6)
runTime = "early"
type = ("projected", "offline")
def handler(fit, beacon, context):
    fit.modules.filteredChargeMultiply(lambda mod: mod.charge.requiresSkill("Missile Launcher Operation"),
                                       "emDamage", beacon.getModifiedItemAttr("damageMultiplierMultiplier"),
                                       stackingPenalties = True)
