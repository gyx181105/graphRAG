import json
import random
import string

def generate_company():
    company = {}
    company['name'] = ''.join(random.choices(string.ascii_letters, k=8)) + ' Company'
    company['type'] = random.choice(['Technology', 'Finance', 'Manufacturing', 'Healthcare', 'Retail'])
    company['size'] = random.choice(['Small', 'Medium', 'Large'])
    company['address'] = ''.join(random.choices(string.ascii_letters + string.digits, k=10)) + ' St.'
    company['founded'] = f"{random.randint(1980, 2022)}-{random.randint(1, 12)}-{random.randint(1, 28)}"
    company['business_area'] = random.choice(['Software Development', 'Financial Services', 'Automobile', 'Pharmaceuticals', 'E-commerce'])
    return company

def generate_relationships(companies):
    relationships = []
    for i in range(len(companies)):
        for j in range(i+1, len(companies)):
            if random.random() < 0.3:  # Randomly decide if there is a relationship
                relationships.append({'source': companies[i]['name'], 'target': companies[j]['name']})
    return relationships

if __name__ == '__main__':
    companies = [generate_company() for _ in range(20)]
    relationships = generate_relationships(companies)

    data = {'companies': companies, 'relationships': relationships}

    with open('company_data.json', 'w') as f:
        json.dump(data, f, indent=4)

    print("Data generated and saved to company_data.json.")
