from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    content = file.read().decode('utf-8')
    lines = content.splitlines()

    groups = {}
    objects_set = set()

    for line in lines:
        line = line.strip()
        if not line or ':' not in line or '#' in line:
            continue
            
        group_id, items_str = line.split(':', 1)
        group_id = group_id.strip()

        items = []
        for item in items_str.split(','):
            item = item.strip()
            if not item:
                continue
            
            # Determine state: 1 for '+', 2 for '-'
            state = 1 if item.startswith('+') else 2
            
            # Extract object ID
            obj_id_str = item.replace('+', '').replace('-', '')
            if obj_id_str.isdigit():
                obj_id = int(obj_id_str)
                items.append({'id': obj_id, 'sign': state, 'is_grey': False})
                objects_set.add(obj_id)

        groups[group_id] = {
            'bg': 'white',
            'items': items
        }

    return jsonify({
        'groups': groups,
        'objects': sorted(list(objects_set))
    })

if __name__ == '__main__':
    app.run(debug=True)
