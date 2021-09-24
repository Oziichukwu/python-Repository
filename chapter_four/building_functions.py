from building import Building, Cohorts, Natives

building = {
    "name": "Semi-colon Village",
    "discription": "This the hub of creativity and intelligence",
    "address": "25, bola-ahmed tinubu road",
        "cohorts": [
            {
                "cohort_name": "cohort_One",
                "discription": "These are the alphas",
                "natives": [
                    {
                        "scn": "001",
                        "first_name": "yinka",
                        "last_name": "bolaji",
                        "sex": "M",
                    },
                     {
                        "scn": "002",
                        "first_name": "gideon",
                        "last_name": "yusuf",
                        "sex": "M",
                    },
                     {
                        "scn": "003",
                        "first_name": "lola",
                        "last_name": "bintu",
                        "sex": "F",
                    }                    
                ]
            },
            {
                "cohort_name": "cohort_Two",
                "discription": "These are the swiss_genetator",
                "natives": [
                    {
                        "scn": "004",
                        "first_name": "kola",
                        "last_name": "kumuyi",
                        "sex": "F",
                    },
                     {
                        "scn": "005",
                        "first_name": "jibola",
                        "last_name": "ruth",
                        "sex": "F",
                    },
                     {
                        "scn": "006",
                        "first_name": "yinkus",
                        "last_name": "bolatunde",
                        "sex": "M",
                    }                    
                ]
            },
            {
                "cohort_name": "cohort_Three",
                "discription": "These are the fighters",
                "natives": [
                    {
                        "scn": "007",
                        "first_name": "kehinde",
                        "last_name": "uranus",
                        "sex": "M",
                    },
                     {
                        "scn": "008",
                        "first_name": "micheal",
                        "last_name": "ogene",
                        "sex": "M",
                    },
                     {
                        "scn": "008",
                        "first_name": "demilola",
                        "last_name": "kolade",
                        "sex": "F",
                    }                    
                ]
            }

        ]
}


def create_building():
    building = Building("name", "discription", "address","cohorts")
    return building

def create_cohort():
    cohorts = Cohorts("name", "description", "natives")    
    return cohorts

def create_native():
    natives = Natives("scn", "first_name", ";last_name", "sex")    
    return natives

def display_natives_information():
    print("=" * 60)
    print("Building Name: ",  building['name'])
    print("Description: ",  building['discription'])
    print("Address: ",  building['address'])
    print("=" * 60)
    print("SCN No. \t| First Name \t| Last Name \t| Sex")
    for cohort in building['cohorts']:  
        print("=" * 60)
        print(cohort["cohort_name"])  
        print(cohort["discription"])
        print("SCN No. \t| First Name \t| Last Name \t| Sex")
  
        print("=" * 60)

        for native in cohort['natives']:
            print(" "+ native['scn']+"\t\t"+native['first_name']+ "\t\t"+ native['last_name']+ "\t\t"+ native['sex'])
display_natives_information()
