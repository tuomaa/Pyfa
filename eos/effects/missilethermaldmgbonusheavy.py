# Used by:
# Implants named like: Heavy Missiles HM (6 of 6)
type = "passive"
def handler(fit, container, context):
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Heavy Missiles"),
                                    "thermalDamage", container.getModifiedItemAttr("damageMultiplierBonus"))
