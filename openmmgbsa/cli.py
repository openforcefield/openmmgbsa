"""
CLI app for openmmgbsa
"""

from .preparation import ReceptorPreparer, LigandPreparer, split_structure
from .parametrization import ReceptorParametrizer, LigandParametrizer, build_syste
from .optimization import OPTIMIZERS


def parse_cli():
    pass


def main():
    args = parse_cli()
    if args.structure:
        receptor, ligand = split_structure(args.structure)
        receptor = ReceptorPreparer.from_object(receptor)
        ligand = LigandPreparer.from_object(ligand)
    else:
        receptor = ReceptorPreparer.from_path(args.receptor)
        ligand = LigandPreparer.from_path(args.ligand)

    parameterized_receptor = ReceptorParametrizer(receptor).parametrize()
    parameterized_ligand = LigandParametrizer(ligand).parametrize()

    system = parameterized_ligand + parameterized_receptor

    opt = OPTIMIZERS[args.optimization](system)
    opt.optimize()
    return opt.report()


if __name__ == "__main__":
    report = main()
    print(report.to_txt())